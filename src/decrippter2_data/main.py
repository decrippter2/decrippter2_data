"""Command line interface of decrippter2_data to validate entries

Creative Commons Legal Code

CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.

For these and/or other purposes and motivations, and without any
expectation of additional consideration or compensation, the person
associating CC0 with a Work (the "Affirmer"), to the extent that he or she
is an owner of Copyright and Related Rights in the Work, voluntarily
elects to apply CC0 to the Work and publicly distribute the Work under its
terms, with knowledge of his or her Copyright and Related Rights in the
Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not
limited to, the following:

  i. the right to reproduce, adapt, distribute, perform, display,
     communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
iii. publicity and privacy rights pertaining to a person's image or
     likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work,
     subject to the limitations in paragraph 4(a), below;
  v. rights protecting the extraction, dissemination, use and reuse of data
     in a Work;
 vi. database rights (such as those arising under Directive 96/9/EC of the
     European Parliament and of the Council of 11 March 1996 on the legal
     protection of databases, and under any national implementation
     thereof, including any amended or successor version of such
     directive); and
vii. other similar, equivalent or corresponding rights throughout the
     world based on applicable law or treaty, and any national
     implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention
of, applicable law, Affirmer hereby overtly, fully, permanently,
irrevocably and unconditionally waives, abandons, and surrenders all of
Affirmer's Copyright and Related Rights and associated claims and causes
of action, whether now known or unknown (including existing as well as
future claims and causes of action), in the Work (i) in all territories
worldwide, (ii) for the maximum duration provided by applicable law or
treaty (including future time extensions), (iii) in any current or future
medium and for any number of copies, and (iv) for any purpose whatsoever,
including without limitation commercial, advertising or promotional
purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
member of the public at large and to the detriment of Affirmer's heirs and
successors, fully intending that such Waiver shall not be subject to
revocation, rescission, cancellation, termination, or any other legal or
equitable action to disrupt the quiet enjoyment of the Work by the public
as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason
be judged legally invalid or ineffective under applicable law, then the
Waiver shall be preserved to the maximum extent permitted taking into
account Affirmer's express Statement of Purpose. In addition, to the
extent the Waiver is so judged Affirmer hereby grants to each affected
person a royalty-free, non transferable, non sublicensable, non exclusive,
irrevocable and unconditional license to exercise Affirmer's Copyright and
Related Rights in the Work (i) in all territories worldwide, (ii) for the
maximum duration provided by applicable law or treaty (including future
time extensions), (iii) in any current or future medium and for any number
of copies, and (iv) for any purpose whatsoever, including without
limitation commercial, advertising or promotional purposes (the
"License"). The License shall be deemed effective as of the date CC0 was
applied by Affirmer to the Work. Should any part of the License for any
reason be judged legally invalid or ineffective under applicable law, such
partial invalidity or ineffectiveness shall not invalidate the remainder
of the License, and in such case Affirmer hereby affirms that he or she
will not (i) exercise any of his or her remaining Copyright and Related
Rights in the Work or (ii) assert any associated claims and causes of
action with respect to the Work, in either case contrary to Affirmer's
express Statement of Purpose.

4. Limitations and Disclaimers.

 a. No trademark or patent rights held by Affirmer are waived, abandoned,
    surrendered, licensed or otherwise affected by this document.
 b. Affirmer offers the Work as-is and makes no representations or
    warranties of any kind concerning the Work, express, implied,
    statutory or otherwise, including without limitation warranties of
    title, merchantability, fitness for a particular purpose, non
    infringement, or the absence of latent or other defects, accuracy, or
    the present or absence of errors, whether or not discoverable, all to
    the greatest extent permissible under applicable law.
 c. Affirmer disclaims responsibility for clearing rights of other persons
    that may apply to the Work or any use thereof, including without
    limitation any person's Copyright and Related Rights in the Work.
    Further, Affirmer disclaims responsibility for obtaining any necessary
    consents, permissions or other rights required for any use of the
    Work.
 d. Affirmer understands and acknowledges that Creative Commons is not a
    party to this document and has no duty or obligation with respect to
    this CC0 or use of the Work.
"""

import argparse
import json
import logging
import sys
from importlib import metadata
from pathlib import Path

import coloredlogs
import jsonschema
from pydantic import BaseModel, ValidationError, model_validator

logger = logging.getLogger("decrippter2_data")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(
    coloredlogs.ColoredFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
logger.addHandler(console_handler)


class SchemaManager(BaseModel):
    """Pydantic-based class to manage validation against json schema

    Attributes:
        schema: path to base specs of the decrippter2_data json schema
    """

    d2_schema: Path = Path(__file__).parent.joinpath("schema/schema.json")

    @model_validator(mode="after")
    def validate_files(self):
        if not self.d2_schema.exists():
            raise ValidationError("Could not find decrippter2_data json schema")
        return self

    @staticmethod
    def read_json(infile: str | Path) -> dict:
        """Read an input json file and perform basic validation

        Arguments:
            infile: the input json file

        Returns:
            A dict resulting from the input json file

        Raises:
            FileNotFoundError: file does not exist
            RuntimeError: file is empty or has incorrect suffix
        """
        if not isinstance(infile, Path):
            infile = Path(infile)

        if not infile.exists():
            raise FileNotFoundError(f"Input file {infile} does not exist.")

        if infile.suffix != ".json":
            raise RuntimeError(f'Input file {infile} has no ".json" suffix.')

        with open(infile) as file_in:
            json_dict = json.load(file_in)

        if not json_dict:
            raise RuntimeError(f"Input file {infile} appears to be empty.")

        return json_dict

    def validate_schema(self, instance: str | Path) -> None:
        """Validate a json file against schema

        Arguments:
            instance: a json file following the decrippter2_data schema

        Raises:
            ValueError: validation of instance against schema led to an error
        """
        try:
            jsonschema.validate(
                instance=self.read_json(instance), schema=self.read_json(self.d2_schema)
            )
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(
                f"SchemaManager: Validation of instance against "
                f"decrippter2_data schema led to an error: {e!s}"
            ) from e
        except Exception as e:
            raise ValueError(f"SchemaManager: an error occurred: {e!s}") from e


def setup_cli(arguments: list) -> argparse.Namespace:
    """Run command line interface using argparse.

    Arguments:
        arguments: specified arguments

    Returns:
        argparse.Namespace object with command line parameters
    """
    parser = argparse.ArgumentParser(
        description=(
            f"'decrippter2_data' CLI using decrippter2_data schema v{metadata.version('decrippter2_data')}."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-i",
        type=str,
        required=True,
        nargs="+",
        help="Specifies one or more input files for validation against schema (separated by whitespace).",
    )

    return parser.parse_args(arguments)


def main(files: list | tuple = ()) -> None:
    """Validate input files against json schema

    Arguments:
        files: a list of files to test against schema

    Returns:
        A bool indicating the outcome of the validation
    """
    manager = SchemaManager()

    for file in files:
        try:
            manager.validate_schema(instance=file)
        except Exception as e:
            logger.fatal(str(e))
            exit(1)

    logger.info(f"Completed validation against MITE schema.")
    exit(0)


def entrypoint():
    """Entrypoint for pyproject project:scripts"""
    args = setup_cli(sys.argv[1:])
    main(args.i)


if __name__ == "__main__":
    entrypoint()
